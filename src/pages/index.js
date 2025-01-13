import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import Heading from '@theme/Heading';
import styles from './index.module.css';
import Translate from '@docusaurus/Translate';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div class="background-circle"></div>
      <div class="background-circle"></div>
      <div class="background-circle-mobile"></div>
      <div className="container head_container">
        
        <Heading as="h1" className="hero__title">
          <Translate>哈喽!</Translate><span>&nbsp;</span><span class="responsive-break"><br/></span><Translate>我是</Translate><span class="i18n_space">&nbsp;</span><span class="i18n-break"><br/></span>
          <span className="hero__title_span"><Translate>核动力岩石</Translate></span>
        </Heading>
        {/* <Heading as="h1" className="hero__title">
          This is {siteConfig.title}
        </Heading> */}
        <p className="hero__subtitle"><Translate>这是我在互联网上的空间</Translate></p>
        {/* <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Go
          </Link>
        </div> */}
        <p align="center">
          <a href="https://skillicons.dev">
          <img className="techstack" src="https://skillicons.dev/icons?i=python,vscode,html,css,notion,markdown&theme=light" />
          </a>
        </p>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}>
      <HomepageHeader />
      {/* <main>
        <HomepageFeatures />
      </main> */}
    </Layout>
  );
}
