<script>
	import { slide } from 'svelte/transition';

	import api from './api';

	export let text;

	// Получение книг

	let books = [];

	function getPosts(data={}) {
		const handlerSuccess = (res) => {
			books = res;

			if (count === 0) {
				setTimeout(function() {count=1;}, 250);
				setTimeout(function() {count=2;}, 500);
				setTimeout(function() {count=3;}, 750);
				setTimeout(function() {count=4;}, 1000);
				setTimeout(function() {count=5;}, 1250);
			}
			// setInterval(function() {if (count < 3) {count++;}}, 250);
		};

		api('search', data, handlerSuccess);
	};

	// Анимация подгрузки

	let count = 0;

	$: if (text.length) {
		getPosts({cont: text});
	} else {
		setTimeout(function() {count=4;}, 250);
		setTimeout(function() {count=3;}, 500);
		setTimeout(function() {count=2;}, 750);
		setTimeout(function() {count=1;}, 1000);
		setTimeout(function() {count=0;}, 1250);
	}
</script>

<div class="books">
<!-- {"books" + (text.length ? "" : " disable")}> -->
	{#each books.slice(0, count) as book, i}
		<div class="book" transition:slide|local>
			<div>{i+1}.</div>
			<div>{book.name}</div>
		</div>
		<br />
	{/each}
</div>

<style>
	.books {
		width: 100%;

		margin-top: 42vh;

		text-align: center;
	}

	@media all and (max-width: 490px) {
		.books {
			margin-top: 53vh;
		}
	}

	/* @media all and (max-width: 390px) {
		.books {
			margin-top: 42vh;
		}
	} */

	/* .disable {
		display: none;
	} */

	.book {
		width: 80vw;
		min-width: 250px;
		max-width: 550px;

		padding: 5px 0 5px 35px;

		text-align: left;
		font-size: 1.5rem;
	}

	.book div:first-child {
		width: 20px;
		vertical-align: top;
	}

	.book div:last-child {
		width: calc(100% - 30px);
	}
</style>