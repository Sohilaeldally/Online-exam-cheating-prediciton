# Online Exam Cheating Detection

**Project Overview**

Online Exam Cheating Detection is a computer vision project designed to detect whether a student is cheating or behaving normally during online exams. The system uses a **ResNet-34** model fine-tuned on a custom Roboflow dataset for accurate classification.

The dataset was annotated and preprocessed on Roboflow, including data augmentation techniques such as rotations, flips, and color adjustments to improve model generalization. The model was trained on two classes:

- `normal`
- `cheating`

The trained model achieves a **validation accuracy of 95.4%** and is ready for deployment to monitor student behavior in real-time.

💾 **Predictions Output**

All predictions are automatically saved in a **JSON file (`predictions.json`)**. This allows you to:

- Track results over time  
- Load predictions for further analysis  

🔗 **Try the Model & View the Full Project:** [Roboflow Universe - Online Exam Cheating Detection](https://universe.roboflow.com/sohila-reda-82dmq/online-exam-cheating-detection-vkvle)
