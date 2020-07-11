import React, { useEffect, useState, createRef } from 'react'
import {
  CCol, CBadge,
  CCard,
  CCardBody,
  CCardHeader,
  CDataTable,
  CButton,
  CRow,
  CSelect,
  CLabel,
  CFormGroup
} from '@coreui/react'

//import usersData from '../users/UsersData'
import APIService from '../../services/APIService'
import AlertService from '../../services/AlertService'

import translate from '../../services/i18n/Translate';
const fields = ['filename', 'description', 'row_count', 'filetype', 'created_at']

class Preprocessing extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      datasets: [],
      columns: [],
      selectedDatasetId: -1
    }
    this.handleDatasetNameChange = this.handleDatasetNameChange.bind(this);
  }

  componentDidMount() {
    this.fetchDatasets();
  }

  handleDatasetNameChange(event) {
    let datasetId = event.target.value
    this.setState({selectedDatasetId: datasetId});
    this.fetchColumns(datasetId);
  }


  async fetchDatasets() {
    await APIService.requests
      .get('dataset/all')
      .then(data => {
        console.log(data.datasets)
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

  async fetchColumns(datasetId) {
    await APIService.requests
      .get('dataset/'+datasetId+'/columns')
      .then(data => {
        console.log(data.columns)
        this.setState({columns: data.columns})

      })
      .catch(data => {
        this.setState({columns: []})
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
            {translate.translate("preprocessing.preprocessing_header")}
          </div>
          <div className="card-body">
            <CCol xs="12" lg="12">
              <CCard>
                <CCardHeader>
                  {translate.translate("preprocessing.choose_dataset")}
                </CCardHeader>
                <CCardBody>
                  <CFormGroup row>
                    <CCol md="3">
                      <CLabel htmlFor="select">{translate.translate("preprocessing.dataset")}</CLabel>
                    </CCol>
                    <CCol xs="12" md="9">
                      <CSelect onChange={this.handleDatasetNameChange} custom name="select" id="select">
                        <option value="0">{translate.translate("preprocessing.please_choose")}</option>

                        {this.state.datasets.map((ds, i) =>
                          <option key={i} value={i}>{ds.filename}</option>

                        )}
                      </CSelect>
                    </CCol>
                  </CFormGroup>

                </CCardBody>
              </CCard>
              <CCard>
                <CCardHeader>
                  {translate.translate("preprocessing.choose_column")}
                </CCardHeader>
                <CCardBody>
                  <CFormGroup row>
                    <CCol md="3">
                      <CLabel htmlFor="select">{translate.translate("preprocessing.column")}</CLabel>
                    </CCol>
                    <CCol xs="12" md="9">
                      <CSelect onChange={this.handleDatasetNameChange} custom name="select" id="select">
                        <option value="0">{translate.translate("preprocessing.choose_column")}</option>

                        {this.state.columns.map((col, i) =>
                          <option key={i} value={i}>{col}</option>

                        )}
                      </CSelect>
                    </CCol>
                  </CFormGroup>

                </CCardBody>
              </CCard>
              <CCard>
                <CCardHeader>
                  {translate.translate("preprocessing.choose_operations")}
                </CCardHeader>
                <CCardBody>

                </CCardBody>
              </CCard>
              <CCard>
                <CCardHeader>
                  {translate.translate("preprocessing.result")}
                </CCardHeader>
                <CCardBody>

                </CCardBody>
              </CCard>

            </CCol>
          </div>
        </div>
      </>
    )
  }
}

export default Preprocessing
