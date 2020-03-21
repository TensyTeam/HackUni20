<script>
	import Search from './Search.svelte';

	let status = 0;
	let text = '';

	function changeStatus(event) {
		status = event.detail.cont;
		console.log(text);
	}
</script>

<main>
	<Search status={status} bind:text={text} on:changeStatus={changeStatus} />
</main>

<style>
	main {
		padding: 8px;
	}
</style>
