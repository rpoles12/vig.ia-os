# Modo quiosque para a sessão escolar

Na página, o VIG.IA OS trata os atalhos de aplicativos e intercepta comandos de navegação que o navegador entrega à sessão. A conta dedicada do Windows restringe o acesso aos outros aplicativos. O Filtro de Teclado é a opção para combinações do sistema que escaparem dessa restrição, incluindo Win + L. A compatibilidade depende da edição do Windows e da política da escola. [Quiosque do Edge](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-configure-kiosk-mode) · [Filtro de Teclado](https://learn.microsoft.com/windows/configuration/keyboard-filter/)

## Quando Win + E abre o Explorador ou Win + L bloqueia o PC

Isso indica que o Windows tratou a combinação antes de o navegador entregar o evento ao jogo. Use Alt + 1 para abrir Arquivos imediatamente. Os primeiros quatro botões da barra de tarefas também mostram seus atalhos Alt ao passar o mouse.

Para impedir o bloqueio da tela na conta dedicada, a TI pode ativar a regra predefinida WindowsL do Filtro de Teclado. O filtro suprime a combinação configurada. Usar Win + E para abrir Arquivos do VIG.IA exige redirecionar a tecla no próprio computador, além da configuração do site. [Regra WindowsL](https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-embedded-keyboardfilterservice) · [Regras do Filtro de Teclado](https://learn.microsoft.com/en-us/windows/configuration/keyboard-filter/keyboardfilter-wmi-provider-reference)

## Preparação pela organização

1. No computador da atividade, confirme a edição em **Configurações → Sistema → Sobre**. No computador consultado durante o desenvolvimento, a edição é Windows 11 Education 25H2, que oferece suporte ao Filtro de Teclado. Confirme a existência do recurso na máquina efetivamente usada na escola.
2. Com uma conta de administração da escola, abra **Configurações → Contas → Outros usuários → Quiosque** e configure uma conta dedicada com o Microsoft Edge no modo **Exibição digital ou sinalização interativa**. Use a URL de produção do jogo e selecione a opção sem reinício por inatividade, se disponível. Saia da conta administrativa e entre na conta do quiosque para testar. [Configurar Acesso Atribuído](https://learn.microsoft.com/en-us/windows/configuration/assigned-access/configure-single-app-kiosk)
3. Confirme a saída da organização antes de restringir teclas. O padrão documentado do Acesso Atribuído é **Ctrl + Alt + Del**. Registre a rota de saída autorizada se a escola usar outra configuração. O painel do VIG.IA OS, com **Ctrl + Shift + O**, prepara uma nova rodada e serve a um propósito diferente da saída da conta do Windows.
4. Se Win + L ou outras combinações ainda interromperem a sessão, peça à TI para aplicar o **Filtro de Teclado** nas contas dos participantes e conferir o acesso administrativo de recuperação. Teste primeiro as combinações necessárias, em especial Win + L, Alt + Tab e Alt + F4. Mantenha a saída da equipe funcional. [Configuração e saída do Filtro de Teclado](https://learn.microsoft.com/windows/configuration/keyboard-filter/)
5. Teste **Win + E** e **Win + 1 a 4** no quiosque. Se essas teclas forem retidas pelo Windows, use **Alt + 1 a 4**. Bloquear um atalho nativo pelo Filtro pode impedir que o navegador receba a combinação, por isso o caminho com Alt deve estar disponível para os participantes.

## Conferência na máquina da atividade

- [ ] O Edge abre o jogo na conta dedicada sem barra de navegação.
- [ ] Durante o tutorial e a investigação, tentar voltar, atualizar, trocar de aplicativo e bloquear a tela. A rodada deve permanecer visível conforme as restrições aplicadas pela TI.
- [ ] Verificar Arquivos, VIG.IA, Registros e Áudios com Alt + 1 a 4. Se o quiosque entregar Win + E e Win + 1 a 4 à página, verificar também esses atalhos.
- [ ] Com um campo de resposta em edição, confirmar que os atalhos de navegação não trocam o aplicativo. Com um documento aberto, Esc deve apenas fechar o documento.
- [ ] Verificar se as telas de apagamento, código e encerramento impedem a abertura dos apps. Na tela final, conferir a opção de rever a recapitulação.
- [ ] Testar separadamente o reinício da rodada pelo painel da equipe e a saída do quiosque pela conta autorizada.

Para desfazer a configuração na máquina, retorne à conta administrativa e remova o quiosque em **Contas → Outros usuários → Quiosque**. A TI deve restaurar também a política do Filtro de Teclado que aplicou para a atividade.
