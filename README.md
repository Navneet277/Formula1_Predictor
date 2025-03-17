# Setting Up `f1env` for F1 Predictions

## 📌 Overview
This guide provides step-by-step instructions to create a **Conda environment (`f1env`)** with the required dependencies to run the **F1 race prediction model** using Jupyter Notebook.

---

## 🏎️ 1. Create the Conda Environment
To set up the `f1env` environment with Python 3.10 or later, run:
```sh
conda create -n f1env python=3.10
```

Then, activate the environment:
```sh
conda activate f1env
```

---

## 📦 2. Install Required Packages
Inside the `f1env` environment, install the necessary Python libraries:
```sh
pip install fastf1 pandas numpy scikit-learn jupyter
```

If you prefer Conda:
```sh
conda install -c conda-forge fastf1 pandas numpy scikit-learn jupyter
```

---

## 📊 3. Add `f1env` to Jupyter Kernels
Ensure Jupyter recognizes the `f1env` environment:
```sh
python -m ipykernel install --user --name=f1env --display-name "Python (f1env)"
```

Now, inside Jupyter, you can select **Python (f1env)** as the kernel.

---

## 🚀 4. Run Jupyter Notebook
Start Jupyter Notebook inside `f1env`:
```sh
jupyter notebook
```

Alternatively, for JupyterLab:
```sh
jupyter lab
```

Inside Jupyter Notebook:
1. Open an existing or new notebook.
2. Go to **Kernel** → **Change Kernel**.
3. Select **"Python (f1env)"**.

---

## 🛠 5. Automatically Use `f1env` for Jupyter
### **For macOS/Linux**
To ensure Jupyter always uses `f1env`, add an alias:
```sh
echo 'alias jupyter="conda activate f1env && jupyter notebook"' >> ~/.zshrc
source ~/.zshrc
```

### **For Windows (PowerShell)**
```sh
echo 'function jupyter { conda activate f1env; jupyter notebook }' >> $PROFILE
```

Now, whenever you type `jupyter`, it will automatically activate `f1env` first.

---

## 🎯 Summary
| Step | Command |
|------|---------|
| **Create Conda Environment** | `conda create -n f1env python=3.10` |
| **Activate Environment** | `conda activate f1env` |
| **Install Dependencies** | `pip install fastf1 pandas numpy scikit-learn jupyter` |
| **Add Jupyter Kernel** | `python -m ipykernel install --user --name=f1env --display-name "Python (f1env)"` |
| **Run Jupyter Notebook** | `jupyter notebook` |
| **Auto-Activate `f1env` for Jupyter** | `alias jupyter="conda activate f1env && jupyter notebook"` (macOS/Linux) |

Now you're ready to run **F1 race predictions** using Jupyter Notebook in the `f1env` environment! 🏎️🚀

---

## 🔗 Additional Resources
- [FastF1 Documentation](https://docs.fastf1.dev/)
- [Jupyter Notebook Guide](https://jupyter.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

