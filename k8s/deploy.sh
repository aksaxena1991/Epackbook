#!/usr/bin/env bash
set -e

echo "==> Pointing Docker to minikube's daemon..."
eval $(minikube docker-env)

echo "==> Building FastAPI app image inside minikube..."
docker build -f app.Dockerfile -t epackbook-api:latest .

echo "==> Applying Kubernetes manifests..."
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/api.yaml

echo "==> Waiting for PostgreSQL to be ready..."
kubectl rollout status deployment/epackbook-postgres -n epackbook --timeout=120s

echo "==> Waiting for API to be ready..."
kubectl rollout status deployment/epackbook-api -n epackbook --timeout=120s

echo ""
echo "✅ Deployment complete!"
echo "Access the API at:"
minikube service epackbook-api -n epackbook --url
