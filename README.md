# REA25_M2-3
Репозиторий для задачи определения показаний на аналоговом приборе
# Структура репозитория
- REA25_M2-3/
  - best.pt
  - C9_M2.html
  - C9_M2.ipynb
  - C9_M3.html
  - C9_M3.ipynb
  - dag.py
  - model.dill
  - README.md
  - yolo.yaml
# Описание файлов репозитория
| Файл | Тип | Описание |
|---|---|---|
| `best.pt` | Веса модели yolov11 | Веса модели yolov11 обученной для распознавания показаний аналогового прибора |
| `yolo.yaml` | yaml файл | Файл с описанием датасета для обучения модели yolo |
| `dag.py` | Python скрипт | Скрипт airflow для запуска обучения модели yolo |
| `model.dill` | dill файл | Обученная модель yolo, сериализованная в dill формат |
| `C9_M2.ipynb` | jupyter notebook | Jupyter notebook с кодом для предобработки датасета |
| `C9_M2.html` | html страница | Jupyter notebook с кодом для предобработки датасета в формате html |
| `C9_M3.ipynb` | jupyter notebook | Jupyter notebook с кодом для обучения модели yolov11 распознавать показания аналогового прибора |
| `C9_M3.html` | html страница | Jupyter notebook с кодом для обучения модели yolov11 распознавать показания аналогового прибора в формате html |
| `README.md` | Markdown | Описание проекта |
