from persona_util import SPECIFIC_BIG5_PERSONA_PROMPT

def specific_persona_generation_with_ocean(o, c, e, a, n):
    persona_dict = {
        # Openness
        "imagination": o,
        "artistic_sensitivity": o,
        "emotional_sensitivity": o,
        "adventure_seeking": o,
        "intellectual_curiosity": o,
        "free_spirited_values": o,

        # Conscientiousness
        "responsibility": c,
        "self_control": c,
        "achievement_orientation": c,
        "orderliness": c,
        "caution": c,
        "perseverance": c,

        # Extraversion
        "sociability": e,
        "activity_level": e,
        "excitement_seeking": e,
        "positive_emotions": e,
        "assertiveness": e,
        "social_adventurousness": e,

        # Agreeableness
        "altruism": a,
        "trust": a,
        "cooperativeness": a,
        "humility": a,
        "empathy": a,
        "tolerance": a,

        # Neuroticism
        "anxiety": n,
        "anger": n,
        "depression": n,
        "self_doubt": n,
        "emotional_volatility": n,
        "stress_sensitivity": n
    }

    return SPECIFIC_BIG5_PERSONA_PROMPT.format(**persona_dict)