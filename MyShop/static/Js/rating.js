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