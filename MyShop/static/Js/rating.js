const ratings = document.querySelectorAll('.rating');

ratings.forEach( rating =>{
  const ratingActive = rating.querySelectorAll('.rating_active')[0];
  const ratingValue = rating.querySelectorAll('.rating_value')[0];
  const ratingActiveWidth = ratingValue.innerHTML/0.05;
  ratingActive.setAttribute('style', `width:${ratingActiveWidth}%`);
});