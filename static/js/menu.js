 // Afectacion al menu para que baje de acuerdo a lo que tenga en el contenido 
 $(document).ready(function() {
    let sidebar = $(".sidebar");
    let mainContent = $("#main-content");

    $(window).scroll(function() {
        let scrollTop = $(window).scrollTop();
        let mainContentTop = mainContent.offset().top;
        let mainContentHeight = mainContent.height();
        let windowHeight = $(window).height();

        if (scrollTop > mainContentTop && scrollTop < mainContentTop + mainContentHeight - windowHeight) {
            sidebar.css("top", scrollTop - mainContentTop);
        } else if (scrollTop <= mainContentTop) {
            sidebar.css("top", 0);
        } else {
            sidebar.css("top", mainContentHeight - windowHeight);
        }
    });
});