import axios from "axios";
export async function getProducts() {
	try {
		const response = await axios.get("/api/products");
		if (response.data) {
			return [response.data.products, response.data.total];
		}
	} catch (err) {
		console.log("error: ", err);
	}
	return [null, null];
}
