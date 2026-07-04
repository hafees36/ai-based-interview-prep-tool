import { useState } from "react";
import { useNavigate } from "react-router-dom";

function getRoleName(role) {
  if (!role) return "Software Engineer";
  if (typeof role === "object") return role.role ?? "Software Engineer";
  return role;
}

function OptionBtn({ label, state, onClick, disabled }) {
  const colors = {
    idle: { bg: "#fff", border: "#e5e7eb", text: "#1f2937", icon: null },
    correct: { bg: "#dcfce7", border: "#16a34a", text: "#15803d", icon: "✓" },
    wrong: { bg: "#fee2e2", border: "#dc2626", text: "#b91c1c", icon: "✗" },
    reveal: { bg: "#fef9c3", border: "#ca8a04", text: "#92400e", icon: "★" },
  };

  const c = colors[state];

  return (
    <button
      onClick={onClick}
      disabled={disabled}
      style={{
        width: "100%",
        textAlign: "left",
        background: c.bg,
        border: `2px solid ${c.border}`,
        borderRadius: 12,
        padding: "13px 18px",
        fontSize: 14,
        fontWeight: state === "idle" ? 500 : 700,
        color: c.text,
        cursor: disabled ? "default" : "pointer",
        display: "flex",
        alignItems: "center",
        gap: 10,
      }}
    >
      {c.icon && (
        <span
          style={{
            width: 20,
            height: 20,
            borderRadius: "50%",
            background: c.border,
            color: "#fff",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontSize: 11,
            fontWeight: 900,
          }}
        >
          {c.icon}
        </span>
      )}
      {label}
    </button>
  );
}

function QuestionCard({ q, index, total, onAnswer }) {
  const [chosen, setChosen] = useState(null);

  const handlePick = (i) => {
    if (chosen !== null) return;
    setChosen(i);
    onAnswer(i, q.correct);
  };

  const getState = (i) => {
    if (chosen === null) return "idle";
    if (i === q.correct) return chosen === i ? "correct" : "reveal";
    if (i === chosen) return "wrong";
    return "idle";
  };

  const answered = chosen !== null;
  const gotRight = chosen === q.correct;

  return (
    <div
      style={{
        background: "#fff",
        border: "1px solid #e5e7eb",
        borderRadius: 20,
        padding: "28px",
        boxShadow: "0 2px 16px rgba(0,0,0,0.05)",
      }}
    >
      <div style={{ display: "flex", gap: 14, marginBottom: 20 }}>
        <div
          style={{
            minWidth: 36,
            height: 36,
            borderRadius: "50%",
            background: answered
              ? gotRight
                ? "#16a34a"
                : "#dc2626"
              : "linear-gradient(135deg,#6366f1,#4f46e5)",
            color: "#fff",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontWeight: 800,
          }}
        >
          {answered ? (gotRight ? "✓" : "✗") : index + 1}
        </div>

        <div>
          <p
            style={{
              fontSize: 11,
              fontWeight: 700,
              color: "#9ca3af",
              textTransform: "uppercase",
            }}
          >
            Question {index + 1} of {total}
          </p>

          <p
            style={{
              fontSize: 15,
              fontWeight: 600,
              color: "#111827",
              lineHeight: 1.6,
            }}
          >
            {q.question}
          </p>
        </div>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
        {q.options.map((opt, i) => (
          <OptionBtn
            key={i}
            label={opt}
            state={getState(i)}
            disabled={answered}
            onClick={() => handlePick(i)}
          />
        ))}
      </div>

      {answered && (
        <div
          style={{
            marginTop: 16,
            padding: "10px 16px",
            borderRadius: 10,
            background: gotRight ? "#f0fdf4" : "#fef2f2",
            fontWeight: 600,
          }}
        >
          {gotRight
            ? "🎉 Correct!"
            : `💡 Correct Answer: ${q.options[q.correct]}`}
        </div>
      )}
    </div>
  );
}

export default function Practice() {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const navigate = useNavigate();

  const generateQuestions = async () => {
    setError("");
    setQuestions([]);
    setAnswers({});

    const raw = localStorage.getItem("resumeData");

    if (!raw) {
      setError("Please upload resume first.");
      return;
    }

    let resumeData;

    try {
      resumeData = JSON.parse(raw);
    } catch {
      setError("Resume data corrupted.");
      return;
    }

    const role = getRoleName(resumeData.role);
    const matchedSkills = resumeData.matched_skills || [];
    const missingSkills = resumeData.missing_skills || [];

    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/generate-questions", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          role,
          matched_skills: matchedSkills,
          missing_skills: missingSkills,
        }),
      });

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error);
      }

      if (!Array.isArray(data.questions)) {
        throw new Error("Invalid questions format.");
      }

      setQuestions(data.questions);
    } catch (err) {
      setError(err.message);
    }

    setLoading(false);
  };

  const handleAnswer = (qIndex, chosen, correct) => {
    setAnswers((prev) => ({
      ...prev,
      [qIndex]: { chosen, correct },
    }));
  };

  const answeredCount = Object.keys(answers).length;
  const correctCount = Object.values(answers).filter(
    (a) => a.chosen === a.correct
  ).length;

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f8fafc",
        fontFamily: "'DM Sans', sans-serif",
      }}
    >
      <div
        style={{
          background: "linear-gradient(135deg,#6366f1,#06b6d4)",
          padding: "60px 24px",
          textAlign: "center",
          color: "#fff",
        }}
      >
        <h1 style={{ fontSize: 48, fontWeight: 800 }}>Practice Questions</h1>
        <p>AI-generated MCQs tailored to your skills</p>
      </div>

      <div style={{ maxWidth: 800, margin: "0 auto", padding: 30 }}>
        {error && (
          <div
            style={{
              background: "#fee2e2",
              padding: 14,
              borderRadius: 12,
              color: "#dc2626",
              marginBottom: 20,
            }}
          >
            {error}
          </div>
        )}

        {answeredCount > 0 && (
          <div
            style={{
              background: "#fff",
              padding: 18,
              borderRadius: 14,
              marginBottom: 20,
              display: "flex",
              justifyContent: "space-between",
            }}
          >
            <span>Answered: {answeredCount}</span>
            <span>Correct: {correctCount}</span>
          </div>
        )}

        <div style={{ textAlign: "center", marginBottom: 30 }}>
          <button
            onClick={generateQuestions}
            disabled={loading}
            style={{
              background: "#4f46e5",
              color: "#fff",
              border: "none",
              padding: "14px 30px",
              borderRadius: 14,
              fontWeight: 700,
              cursor: "pointer",
            }}
          >
            {loading ? "Generating..." : "Generate Questions"}
          </button>

          {questions.length > 0 && (
            <button
              onClick={() => navigate("/mock")}
              style={{
                marginLeft: 12,
                background: "#ea580c",
                color: "#fff",
                border: "none",
                padding: "14px 30px",
                borderRadius: 14,
                fontWeight: 700,
              }}
            >
              Start Mock Interview
            </button>
          )}
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
          {questions.map((q, i) => (
            <QuestionCard
              key={i}
              q={q}
              index={i}
              total={questions.length}
              onAnswer={(chosen, correct) =>
                handleAnswer(i, chosen, correct)
              }
            />
          ))}
        </div>
      </div>
    </div>
  );
}