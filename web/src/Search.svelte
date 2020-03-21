<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	function search() {
		let start = document.querySelector('.start input');
		start.classList.remove('disactive');

		dispatch('changeStatus', {
			cont: 1,
		});
	}

	// function outsearch() {
	// 	let start = document.querySelector('.start input');
	// 	start.classList.add('disactive');
	// }
</script>

<div class="start" on:click={outsearch}>
	<input class="active disactive" on:click={search} placeholder="Привет 😉" />
</div>

<style>
	.start {
		position: fixed;
		top: 0;
		left: 0;
		text-align: center;
		width: 100vw;
		height: 100vh;
		line-height: 85vh;
	}

	.start input {
		padding: 10px 15px;
		border: 1.5px solid #333;
		border-radius: 15px;
		width: 80vw;
		min-width: 250px;
		max-width: 550px;
		font-size: 1.4rem;
		font-weight: 420;
		background-color: #fff;
		outline: none;
		caret-color: #000;
		box-shadow:
			0 1px 4px rgba(0, 0, 0, .3),
			-23px 0 20px -23px rgba(0, 0, 0, .8),
			13px 0 20px -23px rgba(0, 0, 0, .8);
	}

	.active {
		background-color: #c0c0c0 !important;
	}

	.disactive {
		background-color: #fff !important;
	}
</style>
