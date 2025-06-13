const swiper = new Swiper(".mySwiper", {
  autoHeight:false,
  loop:true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  slidesPerView:1,
  loopAddBlanckSlides:true,
  centeredSlides:true,
  setWrapperSize:true,
  updateOnWindowResize:true
});
