# Online Exam Cheating Detection

📌 **Project Overview**

Online Exam Cheating Detection is a computer vision project designed to detect whether a student is cheating or behaving normally during online exams. The system uses a **ResNet-34** model fine-tuned on a custom Roboflow dataset for accurate classification.

**Dataset Details:**  
- Original dataset: 7,141 images  
- After data augmentation: 14,343 images  
- Labels: `normal` and `cheating`  
- Preprocessing: resizing, normalization, rotations, flips, color adjustments  

The trained model achieves a **validation accuracy of 95.4%** and is ready for deployment to monitor student behavior in real-time.

💾 **Predictions Output**  
All predictions are automatically saved in a **JSON file (`predictions.json`)**, which allows you to:  

- Track results over time  
- Load predictions for further analysis  
- Integrate easily with dashboards or other reporting tools  

🔗 **Try the Model & View the Full Project:** [Roboflow - Online Exam Cheating Detection](https://app.roboflow.com/sohila-reda-82dmq/online-exam-cheating-detection-vkvle/models/online-exam-cheating-detection-vkvle/1)
