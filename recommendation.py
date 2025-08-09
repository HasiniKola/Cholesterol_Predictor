def recommend(cholesterol):
    if cholesterol < 200:
        return "✅ Desirable level. Keep up the healthy lifestyle!"
    elif 200 <= cholesterol < 240:
        return "⚠️ Borderline high. Consider reducing saturated fats and increasing fiber."
    else:
        return "🚨 High cholesterol. Consult a doctor and adopt heart-healthy habits."