function mascara()
    {
        v_obj=document.getElementById('id_cpf')
        v_fun=soNumeros
        setTimeout("execmascara()",1)
    }

function execmascara()
    {
        v_obj.value=v_fun(v_obj.value)
    }

function soNumeros(v)
    {
        return v.replace(/\D/g,"")
    }

    
function adicionar_padronizador_cpf()
    {
        document.getElementById('id_cpf').onkeypress=mascara;
        document.getElementById('id_cpf').maxLength=11;
    }