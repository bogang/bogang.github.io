// Editorial minimal JS
(function(){
  // 100vw includes the classic scrollbar, but .wrap centres inside the width that
  // excludes it. Publish the delta so --gutter can land on the same content line.
  function syncScrollbar(){
    var sb = window.innerWidth - document.documentElement.clientWidth;
    document.documentElement.style.setProperty('--sb', (sb > 0 ? sb : 0) + 'px');
  }
  syncScrollbar();
  window.addEventListener('resize', syncScrollbar);

  document.addEventListener('click',function(e){
    if(e.target.closest('.menu-btn')){var n=document.querySelector('.nav-main');if(n)n.classList.toggle('open');}
  });
  /* ---- RFQ form ---------------------------------------------------------
     Posts to Formsubmit so enquiries actually land in a mailbox.
     Two rules we deliberately follow, because the previous version lied:
       1. Never show "received" unless the server confirmed it.
       2. Never clear the form unless the data is safely away.
     If delivery fails, the visitor is told plainly and keeps every entry.
  ------------------------------------------------------------------------ */
  var f=document.getElementById('rfq-form');
  if(f){
    var okBox=document.getElementById('rfq-success');
    var manual=document.getElementById('rfq-manual');
    var btn=document.getElementById('rfq-submit');

    function fields(){
      return Array.prototype.slice.call(f.querySelectorAll('input,select,textarea'));
    }
    function toMailto(to){
      var body=fields().filter(function(el){return el.name&&el.value&&el.type!=='file';})
        .map(function(el){return el.name+': '+el.value}).join('\n');
      var sub=encodeURIComponent('RFQ from hb-film.com — '+((f.querySelector('[name="film_type"]')||{}).value||''));
      return 'mailto:'+encodeURIComponent(to)+'?subject='+sub+'&body='+encodeURIComponent(body);
    }
    function showManual(to){
      var a=manual&&manual.querySelector('a.btn-primary');
      if(a&&to)a.href=toMailto(to);
      if(manual){
        manual.classList.add('show');
        manual.scrollIntoView({behavior:'smooth',block:'center'});
      }
    }

    f.addEventListener('submit',function(ev){
      ev.preventDefault();
      var ok=true,first=null;
      f.querySelectorAll('[required]').forEach(function(el){
        if(!el.value){el.style.borderBottomColor='#c0392b';if(!first)first=el;ok=false;}
        else el.style.borderBottomColor='';
      });
      if(!ok){ if(first)first.scrollIntoView({behavior:'smooth',block:'center'}); return; }

      var to=(f.getAttribute('data-to')||'').trim();
      // Guard against a placeholder address that was never replaced.
      var live=to.indexOf('@')>-1 && to.indexOf('your-')<0;

      // No recipient configured: hand off to the mail client, but do NOT claim
      // success — we cannot know whether a mail client actually opened.
      if(!live){
        window.location.href=toMailto(to||'sales@hb-film.com');
        showManual(to||'sales@hb-film.com');
        return;
      }

      if(btn){btn.disabled=true;btn.textContent='Sending…';}
      var payload={};
      fields().forEach(function(el){ if(el.name&&el.type!=='file') payload[el.name]=el.value; });

      fetch(f.getAttribute('action'),{
        method:'POST',
        headers:{'Content-Type':'application/json','Accept':'application/json'},
        body:JSON.stringify(payload)
      }).then(function(res){
        if(!res.ok) throw new Error('HTTP '+res.status);
      }).then(function(){
        // Safe to claim success and clear only after the server accepted it.
        if(okBox)okBox.classList.add('show');
        f.reset();
        if(okBox)okBox.scrollIntoView({behavior:'smooth',block:'center'});
      }).catch(function(){
        // Real failure: say so, and keep every entry the visitor typed.
        showManual(to);
      }).then(function(){
        if(btn){btn.disabled=false;btn.textContent='Submit Inquiry →';}
      });
    });
  }
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
      var id=a.getAttribute('href');
      if(id.length<2)return;
      var el=document.querySelector(id);
      if(el){e.preventDefault();el.scrollIntoView({behavior:'smooth',block:'start'});}
    });
  });
})();