# Smart-Cooking-assistance-


prepared by: Atha Alghamdi- Aghadir Jammah


‏t هو تطبيق ويب تفاعلي يساعد المستخدمين في إنشاء وصفات طعام بناءً على المكونات التي يملكونها. يعتمد التطبيق على الذكاء الاصطناعي للتعرف على المكونات من الصور واقتراح وصفات مناسبة، مع إمكانية توليد صور للأطباق المقترحة.

المحتويات

	•	المقدمة
	•	المتطلبات
	•	التثبيت
	•	الاستخدام
	•	التقنيات المستخدمة
	•	المساهمة
	•	الترخيص

المقدمة

يقوم التطبيق بتحليل صورة المكونات باستخدام Roboflow، ثم يستخدم Gemini AI لتوليد وصفات بناءً على المكونات المكتشفة. بالإضافة إلى ذلك، يمكنه إنشاء صور للأطباق المقترحة باستخدام Hugging Face Inference API.

المتطلبات

يجب تثبيت الأدوات والمكتبات التالية قبل تشغيل المشروع:
‏	•	Python 3.8+
	•	مكتبات Python المطلوبة:

‏pip install streamlit opencv-python numpy roboflow google-generativeai huggingface_hub


	•	مفتاح API لـ Roboflow
	•	مفتاح API لـ Gemini AI
	•	مفتاح API لـ Hugging Face Inference API

التثبيت

اتبع الخطوات التالية لتثبيت وتشغيل المشروع محليًا:

‏git clone https://github.com/username/smart-cooking-assistant.git
‏cd smart-cooking-assistant
‏pip install -r requirements.txt
‏streamlit run app.py

الاستخدام

	1.	افتح التطبيق من خلال streamlit run app.py.
	2.	اضغط على زر Start وسجّل الدخول باستخدام اسم المستخدم.
	3.	قم برفع صورة تحتوي على مكونات الطعام لديك.
	4.	سيقوم التطبيق بالتعرف على المكونات وعرض قائمة بها.
	5.	اختر المكونات التي تريد استخدامها، ثم اضغط Make Recipes.
	6.	انتظر حتى يتم إنشاء الوصفات وعرض صور الأطباق المقترحة.

التقنيات المستخدمة

‏	•	Streamlit لإنشاء واجهة المستخدم التفاعلية.
‏	•	OpenCV لمعالجة الصور.
‏	•	Roboflow API للتعرف على مكونات الطعام من الصور.
‏	•	Google Gemini AI لتوليد وصفات الطبخ بناءً على المكونات.
‏	•	Hugging Face Inference API لإنشاء صور للأطباق بناءً على الوصفات.
