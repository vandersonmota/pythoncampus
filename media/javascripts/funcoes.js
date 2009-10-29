if (navigator.appName.indexOf('Microsoft') != -1)
    {
        clientNavigator = "IE";
    }
else
    {
        clientNavigator = "Other";
    }
    
function bloquear_caracteres(evnt)
    {
        //Função que permite apenas a digitação de números
        if (clientNavigator == "IE")
            {
                if (evnt.keyCode < 48 || evnt.keyCode > 57)
                    {
                        return false
                    }
            }
        else
            {
                if ((evnt.charCode < 48 || evnt.charCode > 57) && evnt.keyCode == 0)
                    {
                        return false
                    }
            }
    }
    
function adicionar_padronizador_cpf()
    {
        document.getElementById('id_cpf').onkeypress=bloquear_caracteres;
        document.getElementById('id_cpf').maxLength=11;
    }