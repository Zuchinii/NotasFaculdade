Este site permite que os alunos insiram suas três notas e descubram se foram aprovados no semestre. A avaliação segue a seguinte distribuição de peso:

Primeira nota: 30
Segunda nota: 30
Terceira nota: 40
Se a soma ponderada for maior ou igual a 70, o aluno é aprovado. Caso contrário, é reprovado.

☁ Tecnologias Utilizadas
O sistema foi desenvolvido utilizando serviços da AWS:

✅ AWS S3 – Hospeda o front-end estático do site.
✅ AWS Lambda – Processa os cálculos de média e retorna o resultado.
✅ API Gateway – Exposição da API para comunicação entre o front-end e o back-end.

💻 Como Funciona?
1️⃣ O usuário acessa o site hospedado no AWS S3.
2️⃣ Insere suas três notas no formulário.
3️⃣ O site envia os dados para a API Gateway, que aciona uma função AWS Lambda para calcular a média.
4️⃣ O resultado ("Aprovado" ou "Reprovado") é exibido na tela.

Segue o Link para realizar o teste:

http://frontteste.s3-website-sa-east-1.amazonaws.com
