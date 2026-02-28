# superapp-juv-2026-backend
Demo de App Moderna con CICD para despliegue automático en AWS

## Descripción

Este proyecto es una demostración de una aplicación moderna serverless construida con arquitectura de microservicios en AWS. Implementa un sistema de gestión de pedidos que permite registrar órdenes de compra a través de una API REST pública.

## Arquitectura

- **API Gateway**: Endpoint REST regional público para recibir peticiones del frontend
- **Lambda Functions**: Microservicio `order-request` en Python para procesar pedidos
- **DynamoDB**: Base de datos NoSQL para almacenar los pedidos
- **CloudFormation**: Infraestructura como código (IaC) para despliegue automatizado
- **CI/CD**: Pipeline automatizado para despliegue continuo en AWS

## Estructura del Proyecto

```
├── source/microservices/order-request/  # Código de la función Lambda
├── infrastructure/                       # Plantillas CloudFormation
└── cicd/                                # Configuración de pipelines
```

## Funcionalidades

- Registro de pedidos con información del cliente (nombre, ciudad)
- Captura de detalles del producto (nombre, cantidad, precio unitario)
- Cálculo automático del total del pedido
- Almacenamiento persistente en DynamoDB
- API REST con soporte CORS para integración con frontend
