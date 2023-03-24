jQuery(document).ready(function () {
    $('.upper').on('input', setFill);
    $('.lower').on('input', setFill);

    var max = $('.upper').attr('max');
    var min = $('.lower').attr('min');

    function setFill(evt) {
        var valUpper = $('.upper').val();
        var valLower = $('.lower').val();
        if (parseFloat(valLower) > parseFloat(valUpper)) {
            var trade = valLower;
            valLower = valUpper;
            valUpper = trade;
        }

        var width = valUpper * 100 / max;
        var left = valLower * 100 / max;
        $('.fill').css('left', 'calc(' + left + '%)');
        $('.fill').css('width', width - left + '%');

        // Update info
        if (parseInt(valLower) == min) {
            $('.easy-basket-lower').val('0');
        } else {
            $('.easy-basket-lower').val(parseInt(valLower));
        }
        if (parseInt(valUpper) == max) {
            $('.easy-basket-upper').val('256000');
        } else {
            $('.easy-basket-upper').val(parseInt(valUpper));
        }
    }

    // изменяем диапазон цен вручную
    $('.easy-basket-filter-info p input').keyup(function () {
        var valUpper = $('.easy-basket-upper').val();
        var valLower = $('.easy-basket-lower').val();
        var width = valUpper * 100 / max;
        var left = valLower * 100 / max;
        if (valUpper > 256000) {
            var left = max;
        }
        if (valLower < 0) {
            var left = min;
        } else if (valLower > max) {
            var left = min;
        }
        $('.fill').css('left', 'calc(' + left + '%)');
        $('.fill').css('width', width - left + '%');
        // меняем положение ползунков
        $('.lower').val(valLower);
        $('.upper').val(valUpper);
    });
    $('.easy-basket-filter-info p input').focus(function () {
        $(this).val('');
    });
    $('.easy-basket-filter-info .iLower input').blur(function () {
        var valLower = $('.lower').val();
        $(this).val(Math.floor(valLower));
    });
    $('.easy-basket-filter-info .iUpper input').blur(function () {
        var valUpper = $('.upper').val();
        $(this).val(Math.floor(valUpper));
    });

});

const ratings1 = document.querySelectorAll('.rating');

ratings1.forEach(rating => {
    const ratingActive = rating.querySelectorAll('.rating_active')[0];
    const ratingValue = rating.querySelectorAll('.rating_value')[0];
    const ratingActiveWidth = ratingValue.innerHTML / 0.05;
    ratingActive.setAttribute('style', `width:${ratingActiveWidth}%`);
});
const ratings = document.querySelectorAll('.rating_prod');

if (ratings.length > 0) {
    initRatings();
}

function initRatings() {
    let ratingActive, ratingValue;
    for (let index = 0; index < ratings.length; index++) {
        const rating = ratings[index];
        initRating(rating);
    }

    function initRating(rating) {
        initRatingVars(rating);

        setRatingActiveWidth();
    }

    function initRatingVars(rating) {
        ratingActive = rating.querySelector('.rating_active_prod')
        ratingValue = rating.querySelector('.rating_value_prod')
    }

    function setRatingActiveWidth(index = ratingValue.innerHTML) {
        const ratingActiveWidth = index / 0.05;
        ratingActive.style.width = `${ratingActiveWidth}%`;
    }
}