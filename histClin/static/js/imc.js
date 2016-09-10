/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


function constructor()
{
    Imc();
}

function Imc()
 {
                 var num1=parseInt($('#id_talla').val());
                 var num2=parseInt($('#id_peso').val());
                 if(isNaN(num1))
                 {
                     num1=0;
                 }
                 if(isNaN(num2))
                 {
                     num2=0;
                 }
                 var resul=Math.pow((num2/num1),2);
                 
                 
                 $('#id_imc').val(Math.round(resul*100)/100);                
                     
    
 }
 