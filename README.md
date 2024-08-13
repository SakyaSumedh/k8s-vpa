# Kubernetes Vertical Pod Autoscaler

### Install VPA to the cluster:
```
git clone https://github.com/kubernetes/autoscaler.git
cd autoscaler/vertical-pod-autoscaler
git checkout origin/vpa-release-1.0
REGISTRY=registry.k8s.io/autoscaling TAG=1.0.0 ./hack/vpa-process-yamls.sh create
```

### Deploy application to the cluster
```
helm upgrade -i <chart name> ./deploy -n <namespace>
```