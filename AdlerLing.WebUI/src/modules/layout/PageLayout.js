import React from 'react';
import { Layout } from 'antd';
import { Route } from 'react-router-dom'

import { HomeView, LoginView, SignUpView, NavBar} from '../../modules';

const { Content, Footer } = Layout;

class PageLayout extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Layout style={{ minHeight: '100vh' }}>
                <NavBar />
                <Layout>
                    <Content style={{ margin: '0 16px' }}>
                        <div>
                            <Route path='/' exact component={HomeView} />
                            <Route path='/login' exact component={LoginView} />
                            <Route path='/signup' exact component={SignUpView} />
                        </div>
                    </Content>
                    <Footer style={{ textAlign: 'center' }}>
                        AdlerLing 2019
                    </Footer>
                </Layout>
            </Layout>
        );
    };
};

export default PageLayout;