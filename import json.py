import json

def lambda_handler(event, context):
    try:
        # Obtém os dados do corpo da requisição
        body = json.loads(event.get("body", "{}"))

        # Extrai as notas passadas pelo front-end
        nota1 = float(body.get("nota1", 0))
        nota2 = float(body.get("nota2", 0))
        nota3 = float(body.get("nota3", 0))

        # Calcula a soma das notas
        soma = nota1 + nota2 + nota3

        # Determina o resultado
        status = "Aprovado!" if soma >= 70 else "Reprovado"

        # Retorna a resposta em formato JSON
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": ""
            },
            "body": json.dumps({"resultado": status, "soma": soma})
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": ""
            },
            "body": json.dumps({"erro": str(e)})
        }