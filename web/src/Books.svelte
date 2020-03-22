<script>
	import { slide } from 'svelte/transition';

	import api from './api';

	export let text;

	// Получение книг

	let books=[];

	function getPosts(data={}) {
		const handlerSuccess = (res) => {
			books=res;
		};

		api('search', data, handlerSuccess);
	};

	getPosts({cont: text});

	// Анимация подгрузки

	let count = 0;

	$: if (text.length) {
		setInterval(function() {if (count < 3) {count++;}}, 250);
	}
</script>

<div class={"books" + (text.length ? "" : " disable")}>
	{#each books.slice(0, count) as book, i}
		<div class="book" transition:slide|local="{{delay: 10}}">
			<div>{i+1}.</div>
			<div>{book.name}</div>
		</div>
		<br />
	{/each}
</div>

<style>
	.books {
		width: 100%;

		margin-top: 47vh;

		text-align: center;
	}

	.disable {
		display: none;
	}

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