import json
import os
import boto3
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE_NAME')
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    """
    Lambda function para registrar pedidos en DynamoDB
    """
    try:
        # Parsear el body del request
        body = json.loads(event.get('body', '{}'))
        
        # Validar campos requeridos
        required_fields = ['nombre', 'ciudad', 'nombre_producto', 'cantidad', 'precio_unitario']
        for field in required_fields:
            if field not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({
                        'error': f'Campo requerido faltante: {field}'
                    })
                }
        
        # Preparar el item para DynamoDB
        item = {
            'order_id': f"{datetime.now().timestamp()}",
            'nombre': body['nombre'],
            'ciudad': body['ciudad'],
            'nombre_producto': body['nombre_producto'],
            'cantidad': int(body['cantidad']),
            'precio_unitario': Decimal(str(body['precio_unitario'])),
            'total': Decimal(str(body['cantidad'])) * Decimal(str(body['precio_unitario'])),
            'fecha_registro': datetime.now().isoformat()
        }
        
        # Guardar en DynamoDB
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Pedido registrado exitosamente',
                'order_id': item['order_id']
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error al procesar el pedido',
                'details': str(e)
            })
        }
