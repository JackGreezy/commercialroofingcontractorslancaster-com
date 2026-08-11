(function(){
  function preselect(){
    var params=new URLSearchParams(window.location.search);
    var need=params.get('need');
    var select=document.querySelector('select[name="roofNeed"]');
    if(!need||!select)return;
    Array.prototype.some.call(select.options,function(option){
      if(option.value.toLowerCase()===need.toLowerCase()){select.value=option.value;return true;}
      return false;
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',preselect);else preselect();
})();
