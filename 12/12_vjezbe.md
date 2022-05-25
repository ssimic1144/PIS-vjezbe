---
colorlinks:
- true
title: 
- Orkestracija konteinera - minikube
subtitle: 
- Vjezbe 12
author: 
- Srđan Daniel Simić
date: 
- 25.05.2022.
theme:
- Copenhagen

---

# Instalacija minikube-a

Skinuti package s official stranice minikube-a

Instalirati minikube iz paketa

# Instalacija - nastavak

Osim minikube-a potrebno je instalirati *driver* odnosno VM

Najjednostavnije je pomoću VirtualBox-a

# Pokretanje minikube-a klustera

`minikube start --driver=virtualbox`

# Korištenje `kubectl`

Za koristit `kubectl` pomoću minikube-a koristi se sljedeća naredba : 

`minikube kubectl --`

# Korištenje `kubectl` - naredbe

`kubectl create deployment test-dep --image=k8s.gcr.io/echoserver:1.4`

`kubectl expose deployment test-dep --type=NodePort --port=8080`

`kubectl port-forward service/test-dep 7080:8080`

# Još naredbi za minikube

`minikube stop`

`minikube delete`
