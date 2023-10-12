import streamlit as st

st.header('Calculadoras', divider='rainbow')
# st.header('_Streamlit_ is :blue[cool] :sunglasses:')

tab1, tab2, tab3 = st.tabs(["IMC", "Ferro", "Nicotina"])

######### TAB1
with tab1:
   st.title('Calculadora de IMC')

   st.write('Esta é uma calculadora de Índice de Massa Corporal (IMC).')

   # Entrada de peso
   peso = st.number_input('Informe seu peso')

   # Entrada de altura
   altura = st.number_input('Informe sua altura')

   # Botão para calcular o IMC
   if st.button('Calcular IMC'):
      # Cálculo do IMC
      imc = peso / (altura ** 2)
      
      st.write(f'Seu IMC é: {imc:.2f}')
      
      # Interpretando o IMC
      if imc < 18.5:
         st.write('Você está abaixo do peso.')
      elif imc >= 18.5 and imc < 24.9:
         st.write('Seu peso está saudável.')
      elif imc >= 25.0 and imc < 29.9:
         st.write('Você está com sobrepeso.')
      else:
         st.write('Você está obeso.')

######### TAB2
with tab2:
   st.title('Calculadora de Doses de Ferro')

   st.write('Esta é uma calculadora de doses diárias recomendadas de ferro.')

   # Entrada de peso
   peso_ferro = st.number_input('Informe seu peso (em kg)')

   # Entrada de sexo
   sexo = st.radio('Selecione seu sexo', ('Masculino', 'Feminino'), index=None)

   # Botão para calcular a dose
   if st.button('Calcular Dose de Ferro'):
      # Cálculo da dose com base no sexo
      if sexo == 'Masculino':
         dose_ferro = peso_ferro * 0.005
      else:
         dose_ferro = peso_ferro * 0.006
      
      st.write(f'Sua dose diária recomendada de ferro é: {dose_ferro:.2f} mg')

######### TAB3
with tab3:
   st.title('Teste de Fagerström')
   st.write('Este é um teste para avaliar a dependência de nicotina em fumantes.')

   def calcula_dependencia(q1, q2, q3, q4, q5, q6):
      pontos = q1 + q2 + q3 + q4 + q5 + q6
      if pontos >= 0 and pontos <= 2:
         return "Muito Baixa"
      elif pontos == 3 or pontos == 4:
         return "Baixa"
      elif pontos == 5:
         return "Média"
      elif pontos == 6 or pontos == 7:
         return "Elevada"
      elif pontos >= 8 and pontos <= 10:
         return "Muito Elevada"

   st.title("Calculadora de Dependência de Tabagismo")

   q1 = st.radio("Em quanto tempo depois de acordar você fuma o primeiro cigarro?", [0, 1, 2, 3], format_func=lambda x: ["Depois de 60 minutos", "31-60 minutos", "6-30 minutos", "Dentro de 5 minutos"][x], index=None)
   q2 = st.radio("Você acha difícil deixar de fumar em lugares onde é proibido?", [0, 1], format_func=lambda x: ["Não", "Sim"][x], index=None)
   q3 = st.radio("Que cigarro você mais sofreria em deixar?", [0, 1], format_func=lambda x: ["Qualquer um", "O primeiro da manhã"][x], index=None)
   q4 = st.radio("Quantos cigarros você fuma por dia?", [0, 1, 2, 3], format_func=lambda x: ["10 ou menos", "11-20", "21-30", "31 ou mais"][x], index=None)
   q5 = st.radio("Você fuma mais durante as primeiras horas após acordar do que durante o resto do dia?", [0, 1], format_func=lambda x: ["Não", "Sim"][x], index=None)
   q6 = st.radio("Você fuma mesmo estando tão doente que precise ficar de cama quase todo o dia?", [0, 1], format_func=lambda x: ["Não", "Sim"][x], index=None)

   # somatorio = q1 + q2 + q3 + q4 + q5 + q6
   # somatorio = q1 + q2 + q3 + q4 + q5 + q6
   if st.button("Calcular"):
      resultado = calcula_dependencia(q1, q2, q3, q4, q5, q6)
      # st.write(somatorio)
      # st.write(f"Somatorio: {somatorio}")

      st.write(f"Resultado: {resultado}")
