def choose_antibiotic(age, microbe, symptoms, disease, contraindications,
                      renal_function, liver_function, pregnancy,
                      current_medications, local_antibiogram, scores):
    
    # Basic rules engine (you can expand this with real clinical logic)
    recommendations = []
    reasons = []

    if disease == "UTI":
        if pregnancy:
            if "Nitrofurantoin" not in contraindications and renal_function == "normal":
                recommendations.append("Nitrofurantoin")
                reasons.append("Safe in pregnancy and effective for uncomplicated UTI.")
            elif "Amoxicillin" not in contraindications:
                recommendations.append("Amoxicillin")
                reasons.append("Alternative option in pregnancy.")
        else:
            if "TMP-SMX" not in contraindications:
                recommendations.append("TMP-SMX")
                reasons.append("Effective for uncomplicated UTI.")
            if "Ciprofloxacin" not in contraindications:
                recommendations.append("Ciprofloxacin")
                reasons.append("Broad-spectrum coverage for complicated UTI.")

    elif disease == "pneumonia":
        if "CURB-65" in scores and scores["CURB-65"] >= 3:
            if "Ceftriaxone" not in contraindications:
                recommendations.append("Ceftriaxone")
                reasons.append("Severe pneumonia indicated by CURB-65 score.")
            if "Azithromycin" not in contraindications:
                recommendations.append("Azithromycin")
                reasons.append("Covers atypical pathogens.")
        else:
            if "Amoxicillin-Clavulanate" not in contraindications:
                recommendations.append("Amoxicillin-Clavulanate")
                reasons.append("Outpatient treatment option for pneumonia.")

    elif disease == "meningitis":
        if "Cefotaxime" not in contraindications:
            recommendations.append("Cefotaxime")
            reasons.append("Effective against common pathogens for meningitis.")
        if "Vancomycin" not in contraindications:
            recommendations.append("Vancomycin")
            reasons.append("Covers resistant Streptococcus pneumoniae.")

    elif disease == "cellulitis":
        if "Clindamycin" not in contraindications:
            recommendations.append("Clindamycin")
            reasons.append("Good coverage for Gram-positives and anaerobes.")
        if "Cephalexin" not in contraindications:
            recommendations.append("Cephalexin")
            reasons.append("First-line treatment for uncomplicated cellulitis.")

    elif disease == "sepsis":
        if scores.get("SOFA", 0) >= 6:
            if "Piperacillin-Tazobactam" not in contraindications:
                recommendations.append("Piperacillin-Tazobactam")
                reasons.append("Broad-spectrum for high SOFA score.")
            if "Meropenem" not in contraindications:
                recommendations.append("Meropenem")
                reasons.append("Carbapenem option for severe sepsis.")

    elif disease == "otitis media":
        if "Amoxicillin" not in contraindications:
            recommendations.append("Amoxicillin")
            reasons.append("First-line treatment for otitis media.")
        if "Cefdinir" not in contraindications:
            recommendations.append("Cefdinir")
            reasons.append("Alternative oral cephalosporin.")

    # Use antibiogram if available
    if microbe in local_antibiogram:
        bug_data = local_antibiogram[microbe]
        if bug_data:
            sorted_abx = sorted(bug_data.items(), key=lambda x: x[1], reverse=True)
            for abx, perc in sorted_abx:
                if abx not in recommendations and abx not in contraindications and perc >= 80:
                    recommendations.append(abx)
                    reasons.append(f"High local sensitivity ({perc}%) against {microbe}.")

    if not recommendations:
        return ("No clear recommendation based on input. Please consult clinical guidelines.", [])

    return ("Recommended Antibiotics:\n" + "\n".join(f"- {abx}: {reason}" for abx, reason in zip(recommendations, reasons)), recommendations)
