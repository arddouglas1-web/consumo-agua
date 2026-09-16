# Medidor de consumo de água
# Douglas Arruda

# Entrada de Dados
imovel_tipo = input("Digite o tipo de imóvel (casa, apartamento ou comercial) ")
consumo_agua = float(input("Digite o consumo de água mensal (m3) " ))

# Processamento e Saída de Dados
if      imovel_tipo == "comercial":
        print ("Tarifa comercial aplicada, consulte o plano corporativo.")
elif    imovel_tipo  == "apartamento" and consumo_agua < 10: 
        print ("Consumo econômico, excelente controle de água!")
elif    imovel_tipo == "apartamento" or (imovel_tipo == "casa" and consumo_agua < 25) :
        print ("Consumo moderado, dentro do padrão residencial.") 
else:
        print  ("Consumo acima do limite residencial")      

        
          
        
    


