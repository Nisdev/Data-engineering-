
This folder contain the files of the RareDis corpus :
train and dev contains the training and validation files (txt and ann), respectively.

**Source Link to the NLP4RARE corpus :** https://github.com/isegura/NLP4RARE-CM-UC3M

#### **Simple text-based definitions of entity and relation types for NLP4RARE corpus**

**entities**

RAREDISEASE | DISEASE | SYMPTOM | SIGN | SKINRAREDISEASE | ANAPHOR

**relations**

Produces	-------    **Arg1:** RAREDISEASE|DISEASE|SKINRAREDISEASE|ANAPHOR,    **Arg2:** SYMPTOM|SIGN

Increases_risk_of	-------   **Arg1:** RAREDISEASE|DISEASE|SKINRAREDISEASE|ANAPHOR,  **Arg2:** RAREDISEASE|DISEASE|SKINRAREDISEASE|ANAPHOR

Is_a	-------   **Arg1:** RAREDISEASE|DISEASE|SKINRAREDISEASE|ANAPHOR,   **Arg2:** RAREDISEASE|DISEASE|SKINRAREDISEASE|ANAPHOR

Is_acron	-------   **Arg1:** RAREDISEASE|DISEASE|SKINRAREDISEASE,   **Arg2:** RAREDISEASE|DISEASE|SKINRAREDISEASE

Anaphora --------	   **Arg1:** RAREDISEASE|DISEASE|SKINRAREDISEASE|SIGN|SYMPTOM,   **Arg2:** ANAPHOR

Is_synon	--------   **Arg1:** RAREDISEASE|DISEASE|SKINRAREDISEASE|ANAPHOR,   **Arg2:** RAREDISEASE|DISEASE|SKINRAREDISEASE|ANAPHOR
	


