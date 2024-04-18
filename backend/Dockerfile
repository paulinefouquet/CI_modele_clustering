# Utiliser une image Python officielle comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances de l'application
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn pandas requests

# Copier le contenu actuel du répertoire vers le répertoire /app dans le conteneur
COPY . .

# Exposer le port 8000
EXPOSE 8000

# Définir la commande à exécuter lors du démarrage du conteneur
CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]