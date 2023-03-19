var swiper = new Swiper(".mySwiper", {
    direction: "vertical", //슬라이드 수직 정렬
    slidesPerView: 1,      //한번에 보여줄 슬라이드 개수
    spaceBetween: 0,       //슬라이드 사이 여백
    centeredSlides: true, // 1번 슬라이드가 가운데 부터 보이기
    mousewheel: true,      // 마우스 휠로 내리기
    loopAdditionalSlides : 5, // 반복할 슬라이드 갯수
    loop: false, // 반복 재생
    autoplay: { 
        delay: 5000, 
        disableOnInteraction: false,
    }, // autoplay: 자동 재생, delay: 지연시간, disableOnInteractions : false로 설정하면 사용자 상호 작용 (스와이프) 후 자동 재생이 비활성화되지 않으며 상호 작용 후 매번 다시 시작
    pagination: {          
      el: ".swiper-pagination", // 페이지 이동 버튼을 담을 태그
      clickable: true,          // 페이지 이동 버튼 클릭 가능 여부
    },
    navigation: {
        prevEl: '.promotion .swiper-prev', // 이전 요소
        nextEl: '.promotion .swiper-next', // 다음 요소
        }
  });


