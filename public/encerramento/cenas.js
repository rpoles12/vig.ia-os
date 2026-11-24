window.SCENES=window.VIGIA_AUDIO.filter(s=>s.id.startsWith("final")).map(s=>({id:s.id,title:s.titulo,text:s.texto,audio:"../audio/"+s.id+".wav",duration_seconds:s.duracao_segundos}));
