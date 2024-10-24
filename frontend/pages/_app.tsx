import type { AppProps } from 'next/app';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}

