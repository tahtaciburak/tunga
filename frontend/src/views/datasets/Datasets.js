import React, { useEffect, useState, createRef } from 'react'
import {
  CCol, CBadge,
  CCard,
  CCardBody,
  CCardHeader,
  CDataTable,
  CButton,
  CRow
} from '@coreui/react'

//import usersData from '../users/UsersData'
import APIService from '../../services/APIService'
import AlertService from '../../services/AlertService'

import translate from '../../services/i18n/Translate';
const fields = ['filename', 'description', 'row_count', 'filetype', 'created_at']

class Datasets extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      datasets: []
    }
  }

  componentDidMount() {
    this.makeAPIcall();
  }

	goTo(address){
    alert('/#'+address);
		this.props.history.push("/");
	}

  async makeAPIcall() {
    await APIService.requests
      .get('dataset/all')
      .then(data => {
        this.setState({ datasets: data.datasets })
      })
      .catch(data => {
        console.log(data)
        AlertService.Add({
          type: 'alert',
          //message: translate.getText('error.' + data.response.body.error.code),
          level: 'error',
          autoDismiss: 5
        });
      });
  }


  render() {
    return (
      <>
        <div className="card">
          <div className="card-header">
            {translate.translate("datasets.my_datasets")}
          </div>
          <div className="card-body">
            <CCol xs="12" lg="12">
              <CCard>
                <CCardHeader>
                  <CButton color="success">{translate.translate("datasets.import_from_local")}</CButton>
                  <CButton style={{ marginLeft: 10 }} color="warning">{translate.translate("datasets.import_from_url")}</CButton>
                  <CButton style={{ marginLeft: 10 }} color="primary">{translate.translate("datasets.import_from_twitter")}</CButton>
                  <CButton style={{ marginLeft: 10 }} color="danger">{translate.translate("datasets.import_from_api")}</CButton>

                </CCardHeader>
                <CCardBody>
                  {this.state.data}
                  <CDataTable
                    items={this.state.datasets}
                    fields={fields}
                    striped
                    itemsPerPage={10}
                    pagination
                  />
                </CCardBody>
              </CCard>
            </CCol>
          </div>
        </div>
      </>
    )
  }
}

export default Datasets
