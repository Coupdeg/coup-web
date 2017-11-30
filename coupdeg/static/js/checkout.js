$(document).ready(function() {
    
    var navListItems = $('ul.setup-panel li a'),
        allWells = $('.setup-content');

    allWells.hide();

    navListItems.click(function(e)
    {
        e.preventDefault();
        var $target = $($(this).attr('href')),
            $item = $(this).closest('li');
        
        if (!$item.hasClass('disabled')) {
            navListItems.closest('li').removeClass('active');
            $item.addClass('active');
            allWells.hide();
            $target.show();
        }
    });
    
    $('ul.setup-panel li.active a').trigger('click');
    
    // DEMO ONLY //
    $('#activate-step-2').on('click', function(e) {
        $('ul.setup-panel li:eq(1)').removeClass('disabled');
        $('ul.setup-panel li a[href="#step-2"]').trigger('click');
        $(this).remove();
    })
    
    $("#btn-next-to-second").click(function(){
        $("#tab-first").removeClass("pointer-inner-gray text-white");
        $("#tab-first").addClass("pointer-inner-white text-gray");
        $("#tab-first-number").removeClass("border-white");
        $("#tab-first-number").addClass("border-gray check-symbol-green");
        $("#tab-first-number").text('✔');
        $("#shopping_cart").removeClass("show active");
        $("#shopping_cart").addClass("display-none");

        $("#tab-second").removeClass("pointer-inner-white text-gray");
        $("#tab-second").addClass("pointer-inner-gray text-white");
        $("#tab-second-number").removeClass("border-gray");
        $("#tab-second-number").addClass("border-white");        
        $("#shopping_info").removeClass("display-none");
        $("#shopping_info").addClass("show active");
    });

    $("#btn-next-to-third").click(function(){
        $("#tab-second").removeClass("pointer-inner-gray text-white");
        $("#tab-second").addClass("pointer-inner-white text-gray");
        $("#tab-second-number").removeClass("border-white");
        $("#tab-second-number").addClass("border-gray check-symbol-green");
        $("#tab-second-number").text('✔');
        $("#shopping_info").removeClass("show active");
        $("#shopping_info").addClass("display-none");

        $("#tab-third").removeClass("pointer-inner-last-white text-gray");
        $("#tab-third").addClass("pointer-inner-last-gray text-white");
        $("#tab-third-number").removeClass("border-gray");
        $("#tab-third-number").addClass("border-white");
        $("#shopping_payment").removeClass("display-none");
        $("#shopping_payment").addClass("show active");
    });

    $("#btn-back-to-first").click(function(){
        $("#tab-first").removeClass("pointer-inner-white text-gray");
        $("#tab-first").addClass("pointer-inner-gray text-white");
        $("#tab-first-number").removeClass("border-gray check-symbol-green");
        $("#tab-first-number").addClass("border-white");
        $("#tab-first-number").text('1');
        $("#shopping_cart").removeClass("display-none");
        $("#shopping_cart").addClass("show active");

        $("#tab-second").removeClass("pointer-inner-gray text-white");
        $("#tab-second").addClass("pointer-inner-white text-gray");
        $("#tab-second-number").removeClass("border-gray check-symbol-green");
        $("#tab-second-number").addClass("border-gray");
        $("#shopping_info").removeClass("show active");
        $("#shopping_info").addClass("display-none");
    });

    $("#btn-back-to-second").click(function(){
        $("#tab-second").removeClass("pointer-inner-white text-gray");
        $("#tab-second").addClass("pointer-inner-gray text-white");
        $("#tab-second-number").removeClass("border-gray check-symbol-green");
        $("#tab-second-number").addClass("border-white");
        $("#tab-second-number").text('2');
        $("#shopping_info").removeClass("display-none");
        $("#shopping_info").addClass("show active");

        $("#tab-third").removeClass("pointer-inner-last-gray text-white");
        $("#tab-third").addClass("pointer-inner-last-white text-gray");
        $("#tab-third-number").removeClass("border-gray ");
        $("#tab-third-number").addClass("border-gray");
        $("#shopping_payment").removeClass("show active");
        $("#shopping_payment").addClass("display-none");
    });
    $('#my-imageupload').imageupload(options);
});

