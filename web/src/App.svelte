<script>
	let status = 0;

	function start() {
		status = 1;

		let start = document.getElementsByClassName('start')[0];
		start.classList.add('active');
	}
</script>

<main>
	<div class="start">
		<input on:click={start} placeholder="Привет 😉" />
	</div>
</main>

<style>
	main {
		padding: 8px;
	}

	.start {
		position: fixed;
		top: 0;
		left: 0;
		text-align: center;
		width: 100vw;
		height: 100vh;
		cursor: pointer;
		line-height: 85vh;
	}

	.start input {
		padding: 10px 15px;
		border: 1.5px solid #333;
		border-radius: 15px;
		width: 40vw;
		min-width: 250px;
		font-size: 1.4rem;
		font-weight: 420;
		background-color: #fff;
		box-shadow:
			0 1px 4px rgba(0, 0, 0, .3),
			-23px 0 20px -23px rgba(0, 0, 0, .8),
			13px 0 20px -23px rgba(0, 0, 0, .8);
	}

	.active {
		background-color: #c0c0c0;
	}
</style>
