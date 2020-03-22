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
			<table>
				<tr>
					<td>{i+1}.</td>
					<td id="image">
						<img src={book.img} alt={book.name}>
						<button>Купить</button>
					</td>
					<td>
						<h3>{book.name}</h3>
						<p>{book.description}</p>
					</td>
				</tr>
			</table>
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

	.book {
		width: 80vw;
		min-width: 250px;
		max-width: 550px;

		padding: 5px 0 5px 35px;

		text-align: left;
		font-size: 1.5rem;
	}

	.book div {
		box-sizing: border-box;
	}

	.book td:first-child {
		width: 20px;
		vertical-align: top;
	}

	.book td#image {
		width: 150px;
		padding: 10px 25px;
		vertical-align: top;
	}

	.book td#image img {
		width: 100%;
	}

	.book td#image button {
		width: 100%;
		padding: 10px;
		background-color: #ffeaa7;
		cursor: pointer;
		margin-top: 15px;
		border: 0;
	}

	.book td:last-child {
		width: calc(100% - 180px);
	}

	.book td:last-child h3 {
		font-weight: 500;
	}

	.book td:last-child p {
		color: #c0c0c0;
		font-size: 1rem;
	}

	@media all and (max-width: 620px) {
		.book td:first-child {
			display: none;
			width: 0;
		}

		.book td#image {
			display: none;
			width: 0;
		}
	}
</style>