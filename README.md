
# Brain Tumor Segmentation

This project is a **deep learning–based brain tumor segmentation application** that uses a **U-Net** model to detect and segment tumor regions from MRI brain scans.
It provides an **interactive web interface** built with **Streamlit**, allowing users to upload MRI images and visualize the predicted tumor mask instantly.

## Tech Stack
- **Python 3.10**

- **TensorFlow / Keras** – for loading and running the trained U-Net model

- **NumPy** – for numerical and array operations

- **Pillow (PIL)** – for image processing

- **Streamlit** – for building the interactive web application interface
## Dataset Link

Link : https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation
## Deployment

To deploy this project run the below command in your terminal

```bash
    #1. Create your virtual environment

    python -m venv venv
```

```bash
    #2. Activate your virtual environment
    
    venv\Scripts\activatey
```

```bash
    #3. Install dependencies
    
    pip install -r requirements.txt
```

```bash
    #4. Run the Streamlit app
    
    streamlit run app.py
```


## Screenshots

![App Screenshot](https://github.com/booyakabooyaka619/Brain_Tumor_Segmentation/blob/main/bts_pic1.jpeg)

![App Screenshot](https://github.com/booyakabooyaka619/Brain_Tumor_Segmentation/blob/main/bts_pic2.jpeg)


