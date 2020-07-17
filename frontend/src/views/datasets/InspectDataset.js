import React, { useEffect, useState, createRef } from 'react'
import {
  CCol, CBadge,
  CCard,
  CCardBody,
  CCardHeader,
  CDataTable,
  CButton,
  CLabel,
  CRow
} from '@coreui/react'

//import usersData from '../users/UsersData'
import APIService from '../../services/APIService'
import AlertService from '../../services/AlertService'

import translate from '../../services/i18n/Translate';
const fields = ['filename', 'description', 'row_count', 'filetype', 'created_at']

class InspectDataset extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      datasets: []
    }
  }

  componentDidMount() {
    alert(this.props.match.params.id)
    this.makeAPIcall();
  }

	goTo(address){
    alert('/#'+address);
		this.props.history.push("/");
	}

  async makeAPIcall() {
    /*  
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
      });*/
  }


  render() {
    return (
      <>
        <div className="card">
          <div className="card-header">
            {translate.translate("datasets.inspect_dataset")}
          </div>
          <div className="card-body">
            <CCol xs="12" lg="12">
            <CCard>
                <CCardHeader>
                    {translate.translate("datasets.inspect_dataset")}
                </CCardHeader>
                <CCardBody>
                    <CLabel>Test</CLabel>
                </CCardBody>
              </CCard>

              <CCard>
                <CCardHeader>
                    {translate.translate("datasets.inspect_dataset")}
                </CCardHeader>
                <CCardBody>
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

export default InspectDataset
