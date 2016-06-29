django.jQuery(document).ready(function($) {
 $('#id_position_0, #id_position_1').attr('readonly', 'readonly');

 $('#id_Familia_endereco_Rua, #id_Familia_endereco_Numero, #id_Familia_endereco_Bairro, #id_Familia_endereco_Cidade, #id_Familia_Endereco_Estado').blur(function(event) {
  /* Act on the event */
  if ($('#id_Familia_endereco_Rua').val()!='' && $('#id_Familia_endereco_Numero').val()!='' && $('#id_Familia_endereco_Bairro').val()!='' && $('#id_Familia_endereco_Cidade').val()!='' && $('#id_Familia_Endereco_Estado').val()!='') {
   $('.geoposition-search input').val($('#id_Familia_endereco_Rua').val()+' '+$('#id_Familia_endereco_Numero').val()+' '+$('#id_Familia_endereco_Bairro').val()+' '+$('#id_Familia_endereco_Cidade').val()+' '+$('#id_Familia_Endereco_Estado').val());
   
   // TRIGGER DO ENTER PARA EXECUTAR A BUSCA
   var e = $.Event("keydown");
   e.which = 50; // # Some key code value
   $(".geoposition-search input").trigger(e);
  };
 });
})