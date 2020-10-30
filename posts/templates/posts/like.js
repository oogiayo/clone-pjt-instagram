const likeForm = document.querySelector('#like-form')
const postId = likeForm.dataset.postId;
const username = likeForm.dataset.username;

function like(e) {
  e.preventDefault();

  const LIKE_URL = `/posts/`
  const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]');
}


// likeForm.addEventListener('submit', like);
