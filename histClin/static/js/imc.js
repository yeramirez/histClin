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
                 var talla=parseFloat($('#id_talla').val());
                 var peso=parseInt($('#id_peso').val());
                 if(isNaN(talla))
                 {
                     talla=0;
                 }
                 if(isNaN(peso))
                 {
                     peso=0;
                 }
                 
                  talla=Math.pow(talla, 2)
                 
                 
                 var resul=peso/talla;
                 
                 
                 $('#id_imc').val(Math.round(resul*100)/100);                
                     
    
 }
 
 
 
 