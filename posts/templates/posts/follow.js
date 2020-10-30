const followForms = document.querySelectorAll('#follow-form');
const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]');
const config = { headers: {'X-CSRFToken': csrfToken}};


followForms.forEach(followForm => {
  const followBtn = followForm.querySelector('button');
  const username = followForm.dataset.username;
  const API_URL = `/accounts/${username}/follow/`;
  
  function follow(e) {
    e.preventDefault();
    axios.post(API_URL, {}, config)
      .then(response => {
        followBtn.innerText = '팔로우취소';
      })
      .catch(err => {
        console.error(err);
      })
    };

  followForm.addEventListener('submit', follow);
})

