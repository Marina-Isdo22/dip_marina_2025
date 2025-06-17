document.addEventListener('DOMContentLoaded', function () {
  const slider = document.getElementById('price-slider');
  const minInput = document.getElementById('min-price');
  const maxInput = document.getElementById('max-price');
  const resetBtn = document.getElementById('reset-btn');

  if (!slider || !minInput || !maxInput) return;

  noUiSlider.create(slider, {
    start: [parseInt(minInput.value), parseInt(maxInput.value)],
    connect: true,
    range: {
      'min': 100,
      'max': 100000
    },
    step: 100,
    format: {
      to: value => Math.round(value),
      from: value => Number(value)
    }
  });

  slider.noUiSlider.on('update', (values, handle) => {
    if (handle === 0) minInput.value = values[0];
    else maxInput.value = values[1];
  });

  minInput.addEventListener('change', () => {
    slider.noUiSlider.set([minInput.value, null]);
  });

  maxInput.addEventListener('change', () => {
    slider.noUiSlider.set([null, maxInput.value]);
  });

  resetBtn.addEventListener('click', () => {
    slider.noUiSlider.set([100, 100000]);
  });
});
