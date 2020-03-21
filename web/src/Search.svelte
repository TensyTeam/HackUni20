<script>
	export let status;
	export let text;

	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	let triggerOut = false;
	let triggerIn = false;

	function search() {
		dispatch('changeStatus', {
			cont: 1,
		});

		triggerIn = true;
	}

	// function update

	function outsearch() {
		triggerOut = true;
	}

	$: ressearch(triggerIn, triggerOut)

	function ressearch(triggerIn, triggerOut) {
		console.log(triggerIn, triggerOut);
	}
</script>

<div class="start" on:click={outsearch}>
	<input
		placeholder="Привет 😉"
		class={status ? 'active' : 'disactive'}
		bind:value={text}
		on:click={search}
	/>
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
